import eel
import desktop
import main

app_name="html"
end_point="index.html"
size=(700,600)

@eel.expose
def new_translate(en_content,src,dest):
    main.translate(en_content,src,dest)

desktop.start(app_name,end_point,size)