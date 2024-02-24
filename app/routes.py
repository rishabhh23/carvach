from fastapi import APIRouter, HTTPException, Path
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import CarSchema, Request, Response, RequestCar

import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
async def create_car_service(request: RequestCar, db: Session = Depends(get_db)):
    crud.create_car(db, car=request.parameter)
    return Response(status="Ok",
                    code="200",
                    message="Car created successfully").dict(exclude_none=True)


@router.get("/")
async def get_cars(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    _cars = crud.get_car(db, skip, limit)
    return Response(status="Ok", code="200", message="Successfully fetched all data", result=_cars)


@router.patch("/update")
async def update_car(request: RequestCar, db: Session = Depends(get_db)):
    _cars = crud.update_car(db, car_id=request.parameter.id,
                             title=request.parameter.title, description=request.parameter.description)
    return Response(status="Ok", code="200", message="Successfully updated data", result=_cars)


@router.delete("/delete")
async def delete_car(request: RequestCar,  db: Session = Depends(get_db)):
    crud.remove_car(db, car_id=request.parameter.id)
    return Response(status="Ok", code="200", message="Successfully deletef data").dict(exclude_none=True)