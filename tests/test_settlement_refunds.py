from mollie.api.objects.refund import Refund
from mollie.api.objects.settlement import Settlement

from .utils import assert_list_object

SETTLEMENT_ID = 'stl_jDk30akdN'


def test_list_refunds_on_settlement_object(client, response):
    """Retrieve a list of payment refunds of a payment."""
    response.get('https://api.mollie.com/v2/settlements/%s' % SETTLEMENT_ID, 'settlement_single')
    response.get('https://api.mollie.com/v2/settlement/%s/refunds' % SETTLEMENT_ID, 'refunds_list')

    settlement = client.settlements.get(SETTLEMENT_ID)
    assert isinstance(settlement, Settlement)

    refunds = client.settlement_refunds.on(settlement).list()
    assert_list_object(refunds, Refund)
