#! /usr/bin/env python3

from InquirerPy import inquirer
from copier import run_copy

def trexcli():
  rol = inquirer.select(
      message = "Selecciona tu rol:",
      choices = ["Cloud engineer", "Software engineer"]
  ).execute()

  if rol == "Cloud engineer":
    template = inquirer.select(
        message = "Selecciona tu template:",
        choices = ["Crear Modulo", "Setup cliente"]
    ).execute()
    if template == "Crear Modulo":
      run_copy("https://github.com/ingdamiangonzalez/tf-skeleton-module-copier.git", ".")
    if template == "Setup cliente":
      print("no tenemos templates para setup cliente")


  if rol == "Software engineer":
      print("no tenemos templates para ese rol")

  # python3.8 -m venv env
  # source env/bin/activate