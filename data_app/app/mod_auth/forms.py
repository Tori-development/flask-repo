
from flask import request
from os.path import join, dirname

class Login: #class for create a differents function in the page


    def watson_normal():
        json_1 = "hola desde forms"
        json_2 = ""

        return json_1

    """def save_images(self,files,path):
        self.file = files
        self.path = path
        if self.file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if self.file:
            #self.filename = secure_filename(self.file.filename)
            self.file.save(os.path.join(self.path,self.file))

        def allowed_file(self,filename):
            return '.'in self.filename and \
                self.filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS"""
