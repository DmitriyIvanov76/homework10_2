from typing import Union

def whu_is_the_best(user_info: str) -> Union[str, None]:

    if user_info.lower() == 'вова':
       return 'лучший'

    return 'введите Вова'



user_input = input()

print(whu_is_the_best(user_input))