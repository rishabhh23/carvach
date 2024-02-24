from sqlalchemy.orm import Session
from models import Cars
from schemas import CarSchema, Response

# get all data -> GET
def get_car(db: Session, skip: int = 0, limit: int = 100):
    cars = db.query(Cars).offset(skip).limit(limit).all()
    return Response(code="200", status="OK", message="Cars retrieved successfully", result=cars)

# get data by id -> GET
def get_car_by_id(db: Session, car_id: int):
    car = db.query(Cars).filter(Cars.id == car_id).first()
    if car:
        return Response(code="200", status="OK", message=f"Car with ID {car_id} retrieved successfully", result=car)
    else:
        return Response(code="404", status="Not Found", message=f"Car with ID {car_id} not found")

# add data -> POST
def create_car(db: Session, car: CarSchema):
    _car = Cars(company=car.company, model=car.model)
    db.add(_car)
    db.commit()
    db.refresh(_car)
    return Response(code="201", status="Created", message="Car created successfully", result={"id": _car.id})

# remove data -> DELETE
def remove_car(db: Session, car_id: int):
    _car = get_car_by_id(db=db, car_id=car_id)
    if _car.result:
        db.delete(_car.result)
        db.commit()
        return Response(code="204", status="No Content", message=f"Car with ID {car_id} deleted successfully")
    else:
        return Response(code="404", status="Not Found", message=f"Car with ID {car_id} not found")

# update data -> PUT
def update_car(db: Session, car_id: int, company: str, model: str):
    _car = get_car_by_id(db=db, car_id=car_id)

    if _car.result:
        _car.result.company = company
        _car.result.model = model
        db.commit()
        db.refresh(_car.result)
        return Response(code="200", status="OK", message=f"Car with ID {car_id} updated successfully", result=_car.result)
    else:
        return Response(code="404", status="Not Found", message=f"Car with ID {car_id} not found")
