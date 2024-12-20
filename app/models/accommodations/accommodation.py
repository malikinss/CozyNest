from sqlalchemy import DECIMAL, Column, Integer, String, ForeignKey, TIMESTAMP
from config import Base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func


class Accommodation(Base):
    __tablename__ = 'accommodations'

    id = Column(Integer, primary_key=True)

    accommodation_type_id = Column(
        Integer,
        ForeignKey('accommodation_types.id'),
        nullable=False
    )
    owner_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    address_id = Column(Integer, ForeignKey('addresses.id'), nullable=False)

    description = Column(String)
    rooms_number = Column(Integer, default=1)
    max_capacity = Column(Integer, default=1)
    price = Column(DECIMAL(10, 2), nullable=False)  # type: ignore
    status = Column(String, default="active")
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, onupdate=func.now())

    accommodation_type = relationship(
        "AccommodationType", back_populates='accommodation'
    )
    accommodation_sleeping_place = relationship(
        "AccommodationSleepingPlace", back_populates='accommodation'
    )
    accommodation_amenity = relationship(
        "AccommodationAmenity", back_populates='accommodation'
    )
    accommodation_rule = relationship(
        "AccommodationRule", back_populates='accommodation'
    )
    accommodation_availability = relationship(
        "AccommodationAvailability", back_populates='accommodation'
    )
    accommodation_image = relationship(
        "AccommodationImage", back_populates='accommodation'
    )
    address = relationship("Address", back_populates='accommodation')
    user = relationship("User", back_populates="accommodation")
    order = relationship("Order", back_populates="accommodation")
    review = relationship("Review", back_populates="accommodation")

    def __repr__(self):
        return (f"<Accommodation(id={self.id}, "
                f"description='{self.description}', "
                f"price={self.price}, "
                f"rooms_number={self.rooms_number}, "
                f"max_capacity={self.max_capacity}, "
                f"status='{self.status}')>")
