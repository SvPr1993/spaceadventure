import json
import traceback

from django.http import HttpResponse
from django.shortcuts import render
from spaceapp.dto import OutputDTO, InputDTO
from spaceapp.forms import KeplerUserForm
from spaceapp.models import Font
from spaceapp.usecase import save_user_data, upper_string, usecase_get_all_fonts


# Весь блок генерирует страницы html
def base_page(request):
    return render(request, 'spaceapp/base.html')


def project_page(request):
    return render(request, 'spaceapp/project.html')


def develops_page(request):
    return render(request, 'spaceapp/develops.html')


def feedback_page(request):
    return render(request, 'spaceapp/feedback.html')


def GJ504b_page(request):
    return render(request, 'spaceapp/GJ504b_page.html')


def kepler_page(request):
    fonts = usecase_get_all_fonts()
    # Переменная form_data содержит данные введенные пользователем на странице
    if request.method == "POST":
        name = request.POST.get("user_name")
        font = request.POST.get("font")
        input_dto = InputDTO(name=name, font=font)
        result_upper_string = upper_string(input_dto)
        print("DTO", result_upper_string)

        # Дальше идет мой новый код с сохранением формы в джанго админ
        form = KeplerUserForm(request.POST)

        if form.is_valid():
            try:
                form.save()

            except Exception as e:
                print(f"❌ Ошибка при сохранении: {e}")
                print(f"Трассировка: {traceback.format_exc()}")

        else:
            print("❌ Форма невалидна")
            print("Ошибки:", form.errors.as_json())
            print("POST данные:", request.POST)

    else:
        form = KeplerUserForm()

    context = {
        "fonts": fonts,
        "form": form,
    }

    return render(request, 'spaceapp/kepler_page.html', context)

# Прочитать про интерфейсы в книге чистая архитектура (ОБЯЗАТЕЛЬНО!)

def gliese_page(request):
    return render(request, 'spaceapp/gliese_page.html')


def nimro_page(request):
    return render(request, 'spaceapp/nimro_page.html')


def prometheus_page(request):
    return render(request, 'spaceapp/prometheus_page.html')


def tanos_page(request):
    return render(request, 'spaceapp/tanos_page.html')


def chimaira_page(request):
    return render(request, 'spaceapp/chimaira_page.html')


# функция поиска по сайту
def search_box_action(request):
    if request.method == 'POST':
        txt = request.POST.get('txt')
        print(txt.find(''))
        return render(request, 'spaceapp/search.html')
    else:
        pass

# Написать техническое задание к этому проекту, что должно происходить на сайте
