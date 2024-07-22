from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sumarasrsrs669'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///artworks.db'
db = SQLAlchemy(app)


class Artwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(100), nullable=False)

# artwork1 = Artwork(title="Sunset", description="A beautiful sunset over the mountains.", image_file="sunset.jpg")
# artwork2 = Artwork(title="Ocean", description="Waves crashing on the shore.", image_file="ocean.jpg")
#
# db.session.add(artwork1)
# db.session.add(artwork2)
# db.session.commit()
@app.route('/')
def index():
    artworks = Artwork.query.all()
    return render_template('index.html', artworks=artworks)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
