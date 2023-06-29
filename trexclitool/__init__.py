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
        message = "Que deseas hacer hoy?",
        choices = ["Crear un nuevo Modulo!", "Crear infraestructura para un cliente!"]
    ).execute()
    if template == "Crear un nuevo Modulo!":
        destinationFolder = inquirer.text(message="En que carpeta copiamos tu proyecto?").execute()
        run_copy("https://github.com/ingdamiangonzalez/tf-skeleton-module-copier.git", destinationFolder)
    if template == "Crear infraestructura para un cliente!":
        destinationFolder = inquirer.text(message="En que carpeta copiamos tu proyecto?").execute()
        run_copy("https://github.com/ingdamiangonzalez/tf-skeleton-base-infra-copier.git", destinationFolder)



  if rol == "Software engineer":
      print("no tenemos templates para ese rol")

  # python3.8 -m venv env
  # source env/bin/activate
