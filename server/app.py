from flask import request, jsonify
from models import db, City

@app.route('/cities', methods=['POST'])
def create_city():
    data = request.json
    new_city = City(name=data['name'], date_of_visit=data['date_of_visit'],
                    best_memories=data['best_memories'], accomodation=data['accomodation'],
                    user_id=data['user_id'])
    db.session.add(new_city)
    db.session.commit()
    return jsonify({'message': 'City created successfully'}), 201

@app.route('/cities', methods=['GET'])
def get_all_cities():
    cities = City.query.all()
    serialized_cities = [city.serialize() for city in cities]  # Assuming a serialize method in your City model
    return jsonify(serialized_cities), 200

@app.route('/cities/<int:city_id>', methods=['GET'])
def get_city(city_id):
    city = City.query.get(city_id)
    if not city:
        return jsonify({'message': 'City not found'}), 404
    return jsonify(city), 200

@app.route('/cities/<int:city_id>', methods=['DELETE'])
def delete_city(city_id):
    city = City.query.get(city_id)
    if not city:
        return jsonify({'message': 'City not found'}), 404
    db.session.delete(city)
    db.session.commit()
    return jsonify({'message': 'City deleted successfully'}), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)

