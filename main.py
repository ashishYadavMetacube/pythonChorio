from fastapi import FastAPI, Response, Form, Depends
from fastapi.responses import FileResponse
from fillpdf import fillpdfs
from pydantic import BaseModel

app = FastAPI()


class UserInfo(BaseModel):
    name: str
    date: str
    month: str
    year: str
    activities: str
    fav_activity: str
    address: str


def user_info_form(
        name: str = Form(...),
        date: str = Form(...),
        month: str = Form(...),
        year: str = Form(...),
        address: str = Form(...),
        activities: str = Form(...),
        fav_activity: str = Form(...)
) -> UserInfo:
    return UserInfo(name=name, date=date, month=month, year=year, activities=activities, fav_activity=fav_activity,
                    address=address)


activity_check_box_map = {
    'Reading': 'Check Box1',
    'Walking': 'Check Box2',
    'Music': 'Check Box3',
    'Other': 'Check Box4'
}
fav_activity_radio_btn_map = {
    'Reading': '0',
    'Walking': '1',
    'Music': '2',
    'Other': '3'
}


@app.post("/generate-pdf/")
async def generate_pdf(user_info: UserInfo = Depends(user_info_form)):
    activities = user_info.activities
    activities = activities.split(',')

    for i in range(len(activities)):
        if activities[i] in activity_check_box_map:
            activities[i] = activity_check_box_map[activities[i]]

    data_to_filled_in_pdf = {'Name': user_info.name,
                             'Dropdown2': user_info.month,
                             'Dropdown1': user_info.date,
                             'Dropdown3': user_info.year,
                             'Address': user_info.address,
                             'Check Box1': 'Off',
                             'Check Box2': 'Off',
                             'Check Box3': 'Off',
                             'Check Box4': 'Off',
                             'Group6': fav_activity_radio_btn_map[user_info.fav_activity]}
    for activity in activities:
        data_to_filled_in_pdf[activity] = "Yes"

    fillpdfs.write_fillable_pdf('input.pdf', 'output.pdf', data_to_filled_in_pdf)

    fillpdfs.flatten_pdf('output.pdf', 'only_readable.pdf')

    response = FileResponse(path='only_readable.pdf', media_type='application/pdf', filename='user-detail-output.pdf')
    return response

