from main import db


CANICA_AS = "891450052"
CANICA_INVESTOR_AS = "885648312"
TVIST_1_AS = "988844322"


def test_owners():
    owners = db.get_owners(CANICA_AS)

    assert len(owners) == 1
    assert owners[0].owner_name == "TVIST 5 AS"
    assert owners[0].percentage == 100.0
    assert owners[0].owner_type == "company"


def test_holdings():
    expected_holdings = [
        ("911964236", "M62 HOLDING AS", "Ordinære aksjer", 50.0),
        ("914531012", "AKERSVEIEN EIENDOMSINVEST AS", "Ordinære aksjer", 100.0),
        ("915796680", "TOLLBUGATA 8 AS", "Ordinære aksjer", 100.0),
        ("916616120", "CANICA EIENDOM 2 AS", "Ordinære aksjer", 100.0),
        ("917756236", "KABELGATEN 32-40 EIENDOM AS", "Ordinære aksjer", 50.0),
        ("921129548", "GRENSEN 17 AS", "Ordinære aksjer", 100.0),
        ("922906548", "HAVNEPARKEN INVEST AS", "Ordinære aksjer", 100.0),
        ("971126140", "KONGENSGATE 22 AS", "Ordinære aksjer", 100.0),
        ("982057485", "KULLERØD EIENDOM AS", "Ordinære aksjer", 100.0),
        ("989551868", "VINTERBRO NÆRINGSPARK AS", "Ordinære aksjer", 100.0),
        ("992569077", "RÅDHUSGATEN 24 AS", "Ordinære aksjer", 100.0),
    ]

    holdings = db.get_holdings(CANICA_AS)

    assert len(holdings) == len(expected_holdings)
    for h in holdings:
        summary = (h.orgnr, h.company_name, h.share_class, h.percentage)
        assert summary in expected_holdings


def test_summary_holdings_and_owners():
    result = db.get_summary(CANICA_AS)

    assert result["number_of_owners"] == 1
    assert result["number_of_holdings"] == 11


def test_summary_with_foreign_owners():
    result = db.get_summary(CANICA_INVESTOR_AS)

    assert result["number_of_owners"] == 5
    assert result["number_of_holdings"] == 1
    assert result["has_foreign_owners"] is True


def test_summary_with_multiple_share_classes():
    result = db.get_summary(TVIST_1_AS)

    assert result["number_of_owners"] == 2
    assert result["number_of_holdings"] == 1
    assert result["has_multiple_share_classes"] is True
