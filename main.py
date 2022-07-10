from utils import load_candidates, get_all, get_by_pk, get_by_skill
from flask import Flask, request, render_template


def main():
    data = load_candidates("candidates.json")

    app = Flask(__name__)

    def get_candidates():
        return get_all(data)

    app.add_url_rule('/', view_func=get_candidates)

    @app.route("/candidates/<pk>")
    def page_candidates(pk):
        return get_by_pk(pk, data=data)

    @app.route("/skills/<skill_name>")
    def candidates_with_skills(skill_name):
        return get_by_skill(skill_name, data=data)

    app.run()


if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
