# Zadanie: System budowy profilu użytkownika w serwisie społecznościowym

from abc import ABC, abstractmethod


# --- Klasa produktu ---
class UserProfile:
    def __init__(self):
        self.profile_data = {}

    def add_data(self, key, value):
        self.profile_data[key] = value

    def show(self):
        return f"UserProfile: {self.profile_data}"


# --- Interfejs Buildera ---
class UserProfileBuilder(ABC):
    @abstractmethod
    def reset(self):
        pass

    @abstractmethod
    def add_basic_info(self, name, email):
        pass

    @abstractmethod
    def add_profile_picture(self, picture_url):
        pass

    @abstractmethod
    def add_hobbies(self, hobbies):
        pass

    @abstractmethod
    def add_friends_list(self, friends):
        pass

    @abstractmethod
    def get_result(self):
        pass


# --- Konkretny Builder: Minimalny profil ---
class MinimalProfileBuilder(UserProfileBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.profile = UserProfile()

    def add_basic_info(self, name, email):
        self.profile.add_data("name", name)
        self.profile.add_data("email", email)

    def add_profile_picture(self, picture_url):
        pass  # Minimalny profil nie ma zdjęcia profilowego

    def add_hobbies(self, hobbies):
        pass  # Minimalny profil nie ma zainteresowań

    def add_friends_list(self, friends):
        pass  # Minimalny profil nie ma listy znajomych

    def get_result(self):
        return self.profile


# --- Konkretny Builder: Pełny profil ---
class FullProfileBuilder(UserProfileBuilder):
    def __init__(self):
        self.reset()

    def reset(self):
        self.profile = UserProfile()

    def add_basic_info(self, name, email):
        self.profile.add_data("name", name)
        self.profile.add_data("email", email)

    def add_profile_picture(self, picture_url):
        self.profile.add_data("profile_picture", picture_url)

    def add_hobbies(self, hobbies):
        self.profile.add_data("hobbies", hobbies)

    def add_friends_list(self, friends):
        self.profile.add_data("friends", friends)

    def get_result(self):
        return self.profile


# --- Klasa Dyrektora ---
class UserProfileDirector:
    def __init__(self, builder: UserProfileBuilder):
        self.builder = builder

    def construct_minimal_profile(self, name, email):
        self.builder.reset()
        self.builder.add_basic_info(name, email)

    def construct_full_profile(self, name, email, picture_url, hobbies, friends):
        self.builder.reset()
        self.builder.add_basic_info(name, email)
        self.builder.add_profile_picture(picture_url)
        self.builder.add_hobbies(hobbies)
        self.builder.add_friends_list(friends)


# --- Przykład użycia ---
if __name__ == "__main__":
    # Minimalny profil
    minimal_builder = MinimalProfileBuilder()
    director = UserProfileDirector(minimal_builder)
    director.construct_minimal_profile("Jan Kowalski", "jan.kowalski@example.com")
    minimal_profile = minimal_builder.get_result()
    print(minimal_profile.show())

    # Pełny profil
    full_builder = FullProfileBuilder()
    director = UserProfileDirector(full_builder)
    director.construct_full_profile(
        name="Anna Nowak",
        email="anna.nowak@example.com",
        picture_url="https://example.com/picture.jpg",
        hobbies=["reading", "traveling", "cooking"],
        friends=["John Doe", "Jane Smith"]
    )
    full_profile = full_builder.get_result()
    print(full_profile.show())
