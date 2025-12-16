from spaceapp.models import Font


def repo_save_user_data(form_data):
    # answer = {"name": "Вася",
    #          "font": "Times New Romans",
    #          }
    answer = repo_save_user_data(form_data)
    return answer


def repo_get_all_fonts():
    all_fonts = Font.objects.all()
    return all_fonts
