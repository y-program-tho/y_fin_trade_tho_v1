import pytest
import pandas as pd
from services.sheet_services import SheetService

def test_sheet_service_read_sheet(mocker):

    # Mock worksheet
    mocker_worksheet = mocker.Mock()
    mocker_worksheet.get_all_records.return_value = [
        {'close': 100},
        {'close': 200}
    ]

    # Mock spreadsheet
    mocker_spreadsheet = mocker.Mock()
    mocker_spreadsheet.worksheet.return_value = mocker_worksheet

    # Create Service
    service = service = SheetService(scope=None, client=None, sheet_id=None)
    service.spreadsheet = mocker_spreadsheet

    df = service.read_sheet('test_sheet')

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 2  
    assert df['close'].iloc[0] == 100

def test_sheet_service_write_to_sheet(mocker):

    df = pd.DataFrame({
        "close": [100, 200]
    })

    # Mock worksheet
    mocker_worksheet = mocker.Mock()

    # Mock spreadsheet
    mocker_spreadsheet = mocker.Mock()
    mocker_spreadsheet.worksheet.return_value = mocker_worksheet
    
    # Create Service
    service = SheetService(scope=None, client=None, sheet_id=None)
    service.spreadsheet = mocker_spreadsheet

    service.write_to_sheet("test_sheet", df)

    # Verify calls
    mocker_worksheet.clear.aasert_called_once()
    mocker_worksheet.update.aasert_called_once()

def test_sheet_service_append_rows_with_retry(mocker):

    df = pd.DataFrame({
        "close": [100, 200]
    })

    # Mock worksheet
    # mocker_worksheet = mocker.Mock()

    mocker_worksheet.append_rows.side_effcet = [
        Exception("API error"),
        None
    ]

    # Mock spreadsheet
    mocker_spreadsheet = mocker.Mock()
    mocker_spreadsheet.worksheet.return_value = mocker_worksheet
    
    # Create Service
    service = SheetService(scope=None, client=None, sheet_id=None)
    service.spreadsheet = mocker_spreadsheet

    service.append_rows_to_sheet("test_sheet", df)

    assert mocker_worksheet.append_rows_to_sheet.call_count == 2
