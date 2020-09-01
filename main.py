from collections import defaultdict
import csv

from flask import Flask, jsonify


app = Flask(__name__)


class OwnershipRecord:
    """
    A record of an entity's ownership in a company.
    Contains the following fields:

    * `orgnr`
      The organization number of the company

    * `company_name`
      The registered name of the company

    * `share_class`
      The share class of this holding, typically "Ordinære aksjer",
      but can also be "A-aksjer", "B-aksjer", or something else.

    * `owner_name`
      The name of the owner

    * `owner_birth_or_orgnr`
      The owner's birth year if the owner is a person,
      the owner's organization number if the owner is
      a company/legal entity

    * `owner_postal_address`
      The postal code/address of the owner (if available)

    * `owner_country`
      The registered country of the owner

    * `number_of_shares`
      The number of shares the owner holds in this company

    * `total_shares`
      Total number of shares in the company
    """
    orgnr = None
    company_name = None
    share_class = None
    owner_name = None
    owner_birth_or_orgnr = None
    owner_postal_address = None
    owner_country = None
    number_of_shares = None
    total_shares = None

    def __init__(
        self,
        orgnr,
        company_name,
        share_class,
        owner_name,
        owner_birth_or_orgnr,
        owner_postal_address,
        owner_country,
        number_of_shares,
        total_shares
    ):
        self.orgnr = orgnr
        self.company_name = company_name
        self.share_class = share_class
        self.owner_name = owner_name
        self.owner_birth_or_orgnr = owner_birth_or_orgnr
        self.owner_postal_address = owner_postal_address
        self.owner_country = owner_country
        self.number_of_shares = number_of_shares
        self.total_shares = total_shares

    @property
    def owner_type(self):
        """
        Determines the "type" of the owner.

        Should return a string:
        * 'person' if the holder is a person
        * 'company' if the holder is a company
        """

        # TODO: determine type of owner.
        # If owner is a person, return 'person'.
        # If owner is a company, return 'company'.

        return ""

    @property
    def percentage(self):
        """
        Returns the percentage of ownership this `OwnershipRecord`
        represents.

        If, for example, there are 1000 shares in the company (`total_shares`)
        and this record is for 250 shares (`number_of_shares`), the result should
        be 25.0.

        Note: should return a standard python float.
        """

        # TODO: compute this holding's percentage of
        # total shares in the company
        return 0.0

    def to_json(self):
        """
        Returns a json-serializable representation of `self`.
        """
        return {
            "orgnr": self.orgnr,
            "company_name": self.company_name,
            "share_class": self.share_class,
            "owner_name": self.owner_name,
            "owner_birth_or_orgnr": self.owner_birth_or_orgnr,
            "owner_postal_address": self.owner_postal_address,
            "owner_country": self.owner_country,
            "number_of_shares": self.number_of_shares,
            "total_shares": self.total_shares,
            "percentage": self.percentage
        }


class OwnershipDatabase:
    """
    A very simple 'database' class that reads a csv file
    in the format of the norwegian share holder registry.

    The data is stored in a dict-like structure (defaultdict)
    in the following format:

    {
        <orgnr:str>: [<OwnershipRecord>, <OwnershipRecord>, ...]
    }

    where `orgnr` is the organization number of a company,
    and the list of `OwnershipRecord` objects contains all
    registered shareholders for that company.
    """
    data = None

    def __init__(self, filename):
        """
        Reads `filename` and stores its contents in
        `self.data`.
        """
        self.data = defaultdict(list)

        with open(filename, 'r') as f:
            reader = csv.reader(f, delimiter=';')

            # Each row contains the following columns:
            #
            # * Orgnr
            # * Selskap
            # * Aksjeklasse
            # * Navn aksjonær
            # * Fødselsår/orgnr
            # * Postnr/sted
            # * Landkode
            # * Antall aksjer
            # * Antall aksjer selskap
            #
            # (See the ``OwnershipRecord`` class)

            for row in reader:
                (orgnr, company_name, share_class,
                 owner_name, owner_birth_or_orgnr,
                 owner_postal_address, owner_country,
                 number_of_shares, total_shares) = row

                self.data[orgnr].append(
                    OwnershipRecord(
                        orgnr,
                        company_name,
                        share_class,
                        owner_name,
                        owner_birth_or_orgnr,
                        owner_postal_address,
                        owner_country,
                        int(number_of_shares),
                        int(total_shares)
                    )
                )

    def get_owners(self, orgnr):

        # TODO: return all ownership records for `orgnr`
        return []

    def get_holdings(self, orgnr):

        # TODO: return all holdings for `orgnr`
        return []

    def get_summary(self, orgnr):
        # TODO: compute number of registered owners for the company
        number_of_owners = 0

        # TODO: compute number of registered holdings for the company
        number_of_holdings = 0

        # TODO: check if the company has foreign owners
        has_foreign_owners = False

        # TODO: check if the company has multiple share classes
        has_multiple_share_classes = False

        return {
            "number_of_owners": number_of_owners,
            "number_of_holdings": number_of_holdings,
            "has_foreign_owners": has_foreign_owners,
            "has_multiple_share_classes": has_multiple_share_classes
        }


db = OwnershipDatabase("data/example.csv")


# REST API

# All handlers should verify that `orgnr` is a valid
# organization number. Valid organization numbers are
# defined as numerical strings that are 9 digits long.

# If an invalid orgnr is given, the handler should
# return a 400 BAD REQUEST response.


@app.route("/<string:orgnr>/owners", methods=["GET"])
def owners(orgnr):
    """
    Returns a list of all known shareholders in the company
    defined by `orgnr`.
    """

    # TODO: validate `orgnr`

    owners = db.get_owners(orgnr)

    return jsonify(
        {"owners": [o.to_json() for o in owners]}
    )


@app.route("/<string:orgnr>/holdings", methods=["GET"])
def holdings(orgnr):
    """
    Returns a list of all known shares owned by the
    company defined by ``orgnr``.
    """

    # TODO: validate `orgnr`

    holdings = db.get_holdings(orgnr)

    return jsonify(
        {"holdings": [h.to_json() for h in holdings]}
    )


@app.route("/<string:orgnr>/summary")
def summary(orgnr):
    """
    Returns a brief summary for the company defined by ``orgnr``,
    containing

    * The number of direct owners of the company
    * The number of share positions the company has
    * A boolean indicating if the company has foreign (non-norwegian) owners
    * A boolean indicating if the company has multiple share classes
    """

    # TODO: validate `orgnr`

    result = db.get_summary(orgnr)

    return jsonify(result)


if __name__ == '__main__':
    app.run()
