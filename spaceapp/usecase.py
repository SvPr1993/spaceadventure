from spaceapp.repo import repo_save_user_data, repo_get_all_fonts
from spaceapp.dto import InputDTO, OutputDTO


def save_user_data(form_data):
    repo_save_user_data(form_data)
    answer = repo_save_user_data(form_data)
    return answer


def upper_string(input_data: InputDTO) -> OutputDTO:
    name = input_data.name
    font = input_data.font
    name = name.upper()
    font = font.upper()
    output_dto = OutputDTO(name=name, font=font)
    return output_dto


def usecase_get_all_fonts():
    fonts = repo_get_all_fonts()
    return fonts
