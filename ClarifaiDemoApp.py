#!/usr/bin/python3
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from clarifai.client import ClarifaiApi
import json

class Clarifi:

	def client(self, app_id, app_secret):

		return ClarifaiApi(app_id, app_secret)

	def run_using_link(self, app_id, app_secret, link):

		return self.client(app_id, app_secret).tag_urls(link);

	def run_using_file(self, app_id, app_secret, file_path):

		return self.client(app_id, app_secret).tag_image_base64(open(file_path))


class Interface(Frame):

	def __init__(self, parent):

		Frame.__init__(self, parent)

		self.parent = parent
		self.clarifi = Clarifi()

		self.initUI()

	def initUI(self):

		self.parent.title("Clarifai Video Demo")

		self.pack(fill=BOTH, expand=1)
		self.center_window()

		self.title_label()
		self.clarifai_app_id()
		self.clarifai_app_secret()
		self.search_file_button()
		self.or_label()
		self.search_file_link()
		self.run_button()

	def center_window(self):

		self.width = 600
		self.heigth = 400

		sw = self.parent.winfo_screenwidth()
		sh = self.parent.winfo_screenheight()

		x = (sw - self.width)/2
		y = (sh - self.heigth)/2
		self.parent.geometry('%dx%d+%d+%d' % (self.width, self.heigth, x, y))


	def title_label(self):

		Label(self, text="Clarifai API Demo", font=("Helvetica", 30)).place(x=50, y=50)

	def clarifai_app_id(self):

		Label(self, text="APP ID:", font=("Helvetica", 12)).place(x=50, y=120)

		self.clarifai_app_id_text = Text(self, height=1, width=55)
		self.clarifai_app_id_text.config(bd=0,  insertbackground="white", bg="black", fg="white")
		self.clarifai_app_id_text.place(x=130, y=120)

	def clarifai_app_secret(self):

		Label(self, text="APP SECRET:", font=("Helvetica", 12)).place(x=50, y=150)

		self.clarifai_app_secret_text = Text(self, height=1, width=55)
		self.clarifai_app_secret_text.config(bd=0,  insertbackground="white", bg="black", fg="white")
		self.clarifai_app_secret_text.place(x=130, y=150)


	def search_file_link(self):

		Label(self, text="Link:", font=("Helvetica", 18)).place(x=50, y=180)

		self.search_file_link_text = Text(self, height=1, width=70)
		self.search_file_link_text.config(bd=0,  insertbackground="white", bg="black", fg="white")
		self.search_file_link_text.place(x=50, y=210)

	def or_label(self):

		Label(self, text="OR", font=("Helvetica", 18)).place(x=50, y=240)

	def search_file_name(self):
		self.file_path = askopenfilename()
		print(self.file_path)

	def search_file_button(self):

		self.file_path = None

		Button(self, width=10, text="Select a File", command=self.search_file_name).place(x=50, y=270)


	def run_button(self):

		def run_query():
			file_link = self.search_file_link_text.get("1.0",END).strip()
			file_path = self.file_path
			api_id = self.clarifai_app_id_text.get("1.0",END).strip()
			app_secret = self.clarifai_app_secret_text.get("1.0",END).strip()

			if not api_id and not app_secret:
				messagebox.showinfo("Warning", "Fill up both APP ID and APP SECRET fields")
				return

			if not file_link and not file_path:
				messagebox.showinfo("Warning", "Provide a file link, or select a file from your computer")
				return

			dict_data = ""
			if len(file_link) > 0:
				dict_data = self.clarifi.run_using_link(api_id, app_secret, file_link)
			elif len(file_path) > 0:
				dict_data = self.clarifi.run_using_file(api_id, app_secret, file_path)

			data = json.dumps(dict_data, ensure_ascii=False, sort_keys=True, indent=4)

			# Create popup with json response
			json_view = Toplevel(height=600, width=600)
			json_text = Text(json_view, height=600, width=600)
			json_text.insert("end", data)
			json_text.config(state=DISABLED)
			json_text.pack()



		Button(self, width=10, text="Run Query", command=run_query).place(x=250, y=330)

	def close(self):
		self.quit()

def main():

	root = Tk()
	app = Interface(root)
	root.mainloop()


main()
