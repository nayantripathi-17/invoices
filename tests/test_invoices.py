import pytest

@pytest.mark.django_db
def test_get_all_invoices(client):
    response = client.get('/invoices/')

    assert response.status_code == 200

@pytest.mark.django_db
def test_get_invoice_pk(client):
    response = client.get('/invoices/1')
    invoices = response.json()
    
    for invoice in invoices:
        assert invoice['invoice']['invoice'] == 1

    assert response.status_code == 200