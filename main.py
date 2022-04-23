from kaggle_environments import make

env = make("kore_fleets", debug=True)

def main():
    env.run(["hard_rules.py"])
    html_string = env.render(mode="html", width=1000, height=800)
    f = open("environment.html", "w")
    f.write(html_string)
    f.close()


if __name__ == '__main__':
    main()

# https://docs.google.com/document/d/1xXcAzMwHO4m50KZ_WS4n9pOzQeYJ-utXQurMenxlwp8/edit
