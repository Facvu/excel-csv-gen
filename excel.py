import datetime
import os
from flask import Blueprint, make_response, request
import pandas

bp = Blueprint('bp', __name__)


@bp.route('/make-excel', methods=['POST'])
def make_excel():
    json_payload = request.get_json()
    df = pandas.DataFrame(json_payload, index=[0])
    date = datetime.datetime.now().strftime("%Y-%m-%d%H%M%S")
    excel_file = f'file-{date}.xlsx'
    for column in df.columns:
        df[column] = df[column].apply(format_cell)
    df.to_excel(excel_file, index=False)

    response = make_response(open(excel_file, 'rb').read())
    response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    response.headers['Content-Disposition'] = f'attachment; filename=file-{date}.xlsx'
    delete_file(excel_file)

    return response


@bp.route('/make-csv', methods=['POST'])
def make_csv():
    json_payload = request.get_json()
    df = pandas.DataFrame(json_payload)
    date = datetime.datetime.now().strftime("%Y-%m-%d%H%M%S")
    csv_file = f'file-{date}.csv'
    for column in df.columns:
        df[column] = df[column].apply(format_cell)
    df.to_csv(csv_file, index=False)

    response = make_response(open(csv_file, 'rb').read())
    response.headers['Content-Type'] = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    response.headers['Content-Disposition'] = f'attachment; filename=file-{date}.csv'
    delete_file(csv_file)

    return response


def format_cell(cell):
    if isinstance(cell, list):
        cell = [str(item) for item in cell]
        ret = ','.join(cell)
        return ret
    return cell


def delete_file(fname):
    if os.path.exists(fname):
        os.unlink(fname)
