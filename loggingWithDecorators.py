from datetime import datetime

class Log:

    def logging(func):

        def wrapper(*args, **kwargs):
            
            result = func(*args, **kwargs)

            if (result == 'OK'):
                with open("./files/log.txt", "a", encoding= "utf-8") as f:
                    time = datetime.now()
                    f.write(f"[{time}] Correct execution")
                    f.write("\n")
            else:
                with open("./files/log.txt", "a", encoding= "utf-8") as f:
                    time = datetime.now()
                    f.write(f"[{time}] ERROR: {result}")
                    f.write("\n")        

        return wrapper

    @logging
    def myFunction(self, string: str, integer: int):
        try:
            for i in range (1, integer):
                print (string)
            return 'OK'
        except Exception as e:
            return e


dumb = Log()
dumb.myFunction(5,"Jairo")