import tkinter as tk
from tkinter import *
from threading import *
from tkinter import Text, Menu, Label, filedialog
from scholarly import scholarly
import xlsxwriter
import html2text

class ScholarParser:
    def __init__(self, title):
        # set windows title
        self.title = title
        self.path = ""
        self.pathResult = ""
        self.readFilePath = ""
        self.l = []
        self.f = []
        self.filtered = []
        self.counter = 0

        # mainWindows instance
        self.mainWindow = tk.Tk()
        self.mainWindow.title(self.title)
        self.mainWindow.geometry("800x600")

        # menubar
        self.menubar(self.mainWindow)

        # label
        self.label(self.mainWindow, "Start by opening the file.", 10, 10)

        # button to import file
        self.button(self.mainWindow, "Open File...", self.openfile, 10, 10)
       
        # textArea section
        self.inputTxt = Text(self.mainWindow, height = 20, width = 80, padx = 10, pady = 10)
        self.inputTxt.pack()
  
    
        # startParse button
        self.button(self.mainWindow, "Start Parsing", self.startParse, 10, 10)
        self.button(self.mainWindow, "Show Content", self.readFile, 10, 10)
        self.button(self.mainWindow, "Make XLSX file.", self.makeXls, 10, 10)

        # status bar state
        self.statusLabel = self.label(self.mainWindow, "Status", 0, 0) 
        self.statusTxt = Text(self.mainWindow, height = 5, width = 40, padx = 5, pady = 5)
        self.statusTxt.pack()

        # mainWindow's mainloop
        self.mainWindow.mainloop()

    # menu bar method
    def menubar(self, window):
        menubar = Menu(window)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="How To Use?", command=self.testerCommand)
        filemenu.add_command(label="About", command=self.testerCommand)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=window.quit)
        menubar.add_cascade(label="Menu", menu=filemenu)
        window.config(menu=menubar)

    # for future update, threading options
    def threading(self):
        t1 = Thread(target=self.makeXls)
        t1.start()

    # bottom text area
    def text(self, window, height, width, padx, pady):
        textArea = Text(window, height = height,  width = width, padx = padx, pady = pady)
        textArea.pack()

    # print the output of the read text
    def printInput(self):
        varstring = self.inputTxt.get("1.0","end-1c") 
        print(varstring)

    # button method that wil be instanced
    def button(self, window, text, command, padx, pady):
        button = tk.Button(window, text = text, command = command, padx = padx, pady = pady)
        button.pack() 

    # label method to be instanced
    def label(self, window, text, padx, pady):
        label = Label(window, text = text, padx = padx, pady = pady)
        label.pack()

    # read file after being parsed
    def readFile(self):
      tf = open(self.pathResult, "r")
      data = tf.read()
      self.inputTxt.insert("1.0", data)

    # open file method
    def openfile(self):
        try:
            tf = filedialog.askopenfilename(
            initialdir="./", 
            title="Open Text file", 
            filetypes=(("Text Files", "*.txt"),)
            )
            tf = open(tf, 'r')  # or tf = open(tf, 'r')
            self.readFilePath = tf.name
            self.path = tf.name[:-4]
            print(self.readFilePath)
            data = tf.read()
            self.inputTxt.insert("end", data)
            self.statusTxt.insert("1.0", "Success reading file...\n")
            tf.close()
        except:
            self.statusTxt.insert("1.0", "Failed reading file...\n")

    # text area on the south
    def statusbar(self, window, text, padx, pady):
        statusbar = Label(window, text = text, padx = padx, pady = pady, relief=tk.SUNKEN)
        statusbar.pack(side=tk.BOTTOM, fill=tk.X)

    # testing
    def testerCommand(self):
        tk.messagebox.showinfo(title="Information", message="ScholarParser - 1.0.0 - MHadi")

    # start to parse HTML into formatted text
    def startParse(self):
        counter = 0
        counter2 = 0
        self.pathResult = "{}Result.txt".format(self.path)
        html = open("{}.txt".format(self.path)).read()
        save = open(self.pathResult, "a+")
        save.writelines(html2text.html2text(html))

        with open(self.pathResult, "r") as f1:
            self.l.extend(f1.read().split("\n\n"))
            self.f = [x for x in self.l if x.strip()]
            # print(len(l))
            # print(filtered)

        self.inputTxt.delete("1.0", "end")

        for i in range(len(self.f)):
            self.f[i].split('.')
            self.f[i].split('.')
            self.f[i].replace('"', '').replace("'", '').replace("_", " ").replace(".", " ")
            split_ref = self.f[i].split('.')
            self.filtered = [x for x in split_ref if x.strip()]
            self.filtered = list(dict.fromkeys(self.filtered))
            self.inputTxt.insert("end", "No " + str(i) + " " + max(split_ref, key=len)+ "\n\n")
            print("No " + str(i) + " " + max(split_ref, key=len))
    
    # create XLS file.
    def makeXls(self):
        self.result = 0
        self.pathResult = "{}Result.txt".format(self.path)
        html = open("{}.txt".format(self.path)).read()
        save = open(self.pathResult, "a+")
        save.writelines(html2text.html2text(html))

        with open(self.pathResult, "r") as f1:
            self.l.extend(f1.read().split("\n\n"))
            self.f = [x for x in self.l if x.strip()]
            # print(len(l))
            # print(filtered)

        # self.inputTxt.delete("1.0", "end")
        workbook = xlsxwriter.Workbook("{}Xls.xlsx".format(self.path))
        worksheet = workbook.add_worksheet()
        print('finished creating a file')
        for i in range(len(self.f)):
            if(i == 0):
                continue
            k = 0
            self.f[i].split('.')
            self.f[i].split('.')
            self.f[i].replace('"', '').replace("'", '').replace("_", " ").replace(".", " ")
            split_ref = self.f[i].split('.')
            self.filtered = [x for x in split_ref if x.strip()]
            self.filtered = list(dict.fromkeys(self.filtered))
            search_query = scholarly.search_pubs(self.f[i])
            one_row = next(search_query)
            contents = [one_row['bib']['title'], str(one_row['bib']['author']), str(one_row['author_id'])]
            for j in range(len(one_row['bib']['author'])):
                k+=1
                worksheet.write(self.counter+j, 0, one_row['bib']['author'][j])
                worksheet.write(self.counter+j, 1, one_row['bib']['title'])
                print('successfully made 0 1 column for item number '  + str(i) + str(j))

                try:
                    search_query = scholarly.search_author(one_row['bib']['author'][j])
                    author = next(search_query)
                    affi = scholarly.fill(author, sections=['basics', 'indices', 'coauthors'])
                    worksheet.write(self.counter+j, 2, str(affi['affiliation']))
                    print('successfully made 2 column for item number '  + str(i) + str(j))

                    try:
                        worksheet.write(self.counter+j, 3, one_row['pub_url'])
                        
                        try:
                            worksheet.write(self.counter+j, 4, one_row['eprint_url'])
                        
                        except:
                            worksheet.write(self.counter+j, 4, "Link not found")

                    except:
                        worksheet.write(self.counter+j, 3, "Link not found")
                        print('error making 2 column for item number '  + str(i) + str(j))


                except:
                    worksheet.write(i, 2, "Data not found")
                    print('error making 2 column for item number '  + str(i) + str(j))
            
            self.counter+=k
            
        workbook.close()

if __name__ == "__main__":
    # window name
    scholarParser = ScholarParser("ScholarParser - 1.0.0")
