import luigi

#substitions from https://xkcd.com/1288/
substitutions = {
    "witnesses": "these dudes I know",
    "allegedly": "kinda probably",
    "new study": "tumblr post",
    "rebuild": "avenge",
    "space": "spaaace",
    "google glass": "virtual boy",
    "smartphone": "pokedex",
    "electric": "atomic",
    "senator": "elf-lord",
    "car": "cat",
    "election": "eating contest",
    "congressional leaders": "river spirits",
    "homeland security": "homestar runner",
    "could not be reached for comment": "is guilty and everyone knows it"
}


def get_input_file():
    return "/usr/local/luigi/datafiles/example1.txt"

# write your task classees here to do XKCD substitutions
# when you are done, you can run them using docker exec pycon2018luigi_scheduler_1 python3 dags/part1.py <TaskClassName>
# the visualizer is located at localhost:8082 where you can check on your dag's progress
#
# Tip: it will be easiest to write your output in /usr/local/luigi/output
# you can read it using docker exec pycon2018luigi_scheduler_1 cat <your_output_file>

class SourceFileTask(luigi.Task):
    def output(self):
        return luigi.LocalTarget(get_input_file())


class SubstitutionTask(luigi.Task):
    def requires(self):
        return SourceFileTask()

    def output(self):
        return luigi.LocalTarget('/usr/local/luigi/output/exercise2.txt')

    def run(self):
        with self.input().open('r') as examplefile:
            text = examplefile.read()

        for old, new in substitutions.items():
            text = text.replace(old, new)

        with self.output().open('w') as outfile:
            outfile.write(text)


def replace(word):
    return substitutions.get(word, word)




if __name__ == "__main__":
    luigi.run()