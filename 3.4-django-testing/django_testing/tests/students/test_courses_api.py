import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Student, Course

@pytest.fixture
def client():
    return APIClient()


# @pytest.fixture
# def user():
#     return User.objects.create_user('admin')


# @pytest.fixture
# def student_factory():
#     def factory(*args, **kwargs):
#         return baker.make(Student, *args, **kwargs)
#     return factory

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.mark.django_db
def test_get_course(client, course_factory):
    # Arrange
    course = course_factory(_quantity=10)

    # Act 
    # проверка фильтрации списка курсов по id
    response_retrieve = client.get('/api/v1/courses/', {'id': 1})
    # проверка фильтрации списка курсов по name
    response_retrieve_name = client.get('/api/v1/courses/', {'name': course[0].name})

    # проверка получения 1го курса (retrieve-логика)
    # проверка получения списка курсов (list-логика)
    response_list = client.get('/api/v1/courses/')

    # Assert
    assert response_retrieve.status_code == 200
    assert response_list.status_code == 200
    assert response_retrieve_name.status_code == 200

    data_retrieve = response_retrieve.json()
    data_retrieve_name = response_retrieve_name.json()
    data_list = response_list.json()

    assert len(data_retrieve) == 1
    assert len(data_retrieve_name) == 1
    assert len(data_list) == len(course)

    assert data_retrieve[0]['name'] == course[0].name
    assert data_retrieve_name[0]['name'] == course[0].name
    for i, m in enumerate(data_list):
        # проверка получения 1го курса (retrieve-логика)
        assert m['name'] == course[i].name


# тест успешного создания курса
@pytest.mark.django_db
def test_post_course(client):
    # Arrange
    count = Course.objects.count()
    data_post = {
        'name': 'mathematics'
    }

    # Act 
    response = client.post('/api/v1/courses/', data_post, format='json')

    # Assert
    assert response.status_code == 201
    assert Course.objects.count() == count + 1

# тест успешного обновления курса
# сначала через фабрику создаем, потом обновляем JSON-данными
@pytest.mark.django_db
def test_patch_course(client, course_factory):
    # Arrange
    course = course_factory(_quantity=1)
    count = Course.objects.count()
    print(f'{count}')

    # Act 
    data_post = {
        'name': 'mathematics'
    }

    response = client.patch(f'/api/v1/courses/{Course.objects.first().id}/', data_post, format='json')

    # Assert
    assert response.status_code == 200
    assert Course.objects.count() == count
    data = response.json()


# тест успешного удаления курса
@pytest.mark.django_db
def test_delete_course(client, course_factory):
    # Arrange
    course = course_factory(_quantity=1)

    # Act 
    response = client.delete(f'/api/v1/courses/{Course.objects.first().id}/')

    # Assert
    assert response.status_code == 204
    assert Course.objects.count() == 0
