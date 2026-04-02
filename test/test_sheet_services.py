from services.sheet_services import SheetService

def test_sheet_service_started():

    sheet_service = SheetService()

    assert 'y_fin_trade_tho_data' in str(sheet_service.sheet)  