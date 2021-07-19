from engine import FileEngine, TemplateEngine
from sys import argv
template_path = argv[1]
log_path = argv[2]

log = FileEngine(log_path).run()
template = TemplateEngine(template_path).run()

for line in log:
    response = template(line)
    if response != None:
        print("".join(f"{key}: {value}\n" for key, value in response.items()))