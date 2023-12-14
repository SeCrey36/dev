<html>
    <head>
        <title>Проект "Autoavia"</title>
    </head>
    <body>
        <h1 align="center">**_Проект "Autoavia"_**</h1>

        <h3 align="center">Дальнейшее развитие проекта:</h3>
        * [] GUI-интерфейс
        * [] DATABASE для запоминания информации о текущих самолетах
        * [] Интерфейс для пользователя в WEB без админских прикольчиков
        * [] Купить мини системный блок с минимальным потреблением для использования в роли сервера
        * [] Базу данных и веб страничку грузить на сервер


        <h3 align="center">Переделать функционал:</h3>
        ```def select_airplane(self):
                """
                Select airplane.

                This function selects an airplane for further operation
                from the list of airplanes

                Raises:
                    IndexError, ValueError

                Examples:
                    airplanes = [plane1, plane2]
                    airplane = None
                    >>> select_airplane()
                    '0 plane1
                    1 plane2'
                    >>> 'Input number of plane: 0'
                    airplanes = [plane1, plane2]
                    airplane = plane1
                """
                try:
                    for i, pl_class in enumerate(self.airplanes):
                        print(i, pl_class.name)
                    self.airplane = self.airplanes[int(input('Input number of plane: '))]
                except IndexError:
                    print('Index Error / 0 airplanes')
                except ValueError:
                    print('Input must be int')```


        <h3 align="center">Расчет стоимости билета по формуле</h3>
        $`эконом = коэф.востребованности * 10`$
        $`бизнес = коэф.востребованности * 20`$
        $`элита = коэф.востребованности * 30`$

        <h3 align="center">Статьи для чтения</h3>
        <a href="https://habr.com/ru/companies/amvera/articles/754702/" target="_self">Базы данных</a>
        <a href="https://habr.com/ru/articles/724650/" target="_self">Сервер</a>
        <img src="smileface.jpg">
    </body>
</html>