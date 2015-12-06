from flask import Blueprint
main_blue=Blueprint('main',__name__)

main=main_blue
import views,errors
