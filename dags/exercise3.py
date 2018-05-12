import luigi

substitutions1288 = {
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

substitutions1625 = {
    "debate": "dance-off",
    "self driving": "uncontrollably swerving",
    "poll": "psychic reading",
    "candidate": "airbender",
    "drone": "dog",
    "vows to": "probably won't",
    "at large": "very large",
    "successfully": "suddenly",
    "expands": "physically expands",
    "first-degree": "friggin' awful",
    "second-degree": "friggin' awful",
    "third-degree": "friggin' awful",
    "an unknown number": "like hundreds",
    "front runner": "blade runner",
    "global": "spherical",
    "years": "minutes",
    "minutes": "years",
    "no indication": "lots of signs",
    "urged restraint by": "drunkenly egged on",
    "horsepower": "tons of horsemeat"
}


def get_input_file():
    return "/usr/local/luigi/datafiles/example1.txt"

# use parameters to determine which set up substitutions to perform
# all available parameter types are available here: http://luigi.readthedocs.io/en/stable/api/luigi.parameter.html
#
# Tip: you may want to use a new output file
class SourceTextTask(luigi.ExternalTask):
    path = luigi.Parameter()

    def output(self):
        return luigi.LocalTarget(self.path)

class SubstitutionTask2(luigi.Task):
    sub_group = luigi.ChoiceParameter(var_type=int, choices=[1625, 1288])


    def requires(self):
        return SourceTextTask(path=get_input_file())

    def run(self):
        subs = {1625: substitutions1625, 1288: substitutions1288}
        chosen = subs[self.sub_group]
        with self.input().open('r') as infile, self.output().open('w') as outfile:
            text = infile.read()
            for old, new in chosen.items():
                text = text.replace(old, new)
            outfile.write(text)
            print(text)

    def output(self):
        return luigi.LocalTarget('/usr/local/luigi/output/exercise3.txt')


if __name__ == "__main__":
    luigi.run()