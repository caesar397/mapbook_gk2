from bs4 import BeautifulSoup
import requests
from mapbook_lib.model import users
import folium


def print_users(users_data: list) -> None:
    for user in users_data:
        print(f'Twoj znajomy {user['name']} z miejscowosci {user['location']} opublikował post "{user['posts'][-1]}"')


def add_user(users_data: list) -> None:
    users_data.append({
        "name": input("Podaj Imie: "),
        "location": input("Podaj swoją lokalizację: "),
        "posts": ["Dołączyłem do mapbooka"]
    })

def remove_user(users_data: list) -> None:
    user_to_remove = input("Podaj imie znajomego do usunięcia: ")
    for user in users_data:
        if user["name"] == user_to_remove:
            users.remove(user)

def update_user(users_data: list) -> None:
    user_to_update = input("Podaj imie znajomego do aktualizacji: ")
    for user in users_data:
        if user["name"] == user_to_update:
            user["name"] = input("Podaj nowe imię użytkownika: ")
            user["location"] = input("Podaj nową lokalizację użytkownika: ")

def update_user_post(users_data: list) -> None:
    user_to_update = input("Podaj imie znajomego do aktualizacji: ")
    for user in users_data:
        if user["name"] == user_to_update:
            user["posts"].append(input("Co słychać?: "))



def get_coordinates(location: str) -> list:
    url = f"https://pl.wikipedia.org/wiki/{location}"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    respoonse_html = BeautifulSoup(response.text, 'html.parser')
    latitude = respoonse_html.select('.latitude')[1].text.replace(",", ".")
    longitude = respoonse_html.select('.longitude')[1].text.replace(",", ".")
    return [latitude, longitude]

def get_user_map(users_data: list) -> None:
    m = folium.Map([52.23, 21], zoom_start=6)

    for user in users_data:
        folium.Marker(
            location=get_coordinates(user["location"]),
            tooltip=user["name"],
            popup=user["posts"][-1],
            icon=folium.Icon(icon="cloud"),
        ).add_to(m)

    m.save("mapa_znajomych.html")