from sqlalchemy import Column, Integer, String, Boolean, Date, Time, DateTime, func
from sqlalchemy.orm import relationship
from app.database import Base

class MedicationReminder(Base):
    __tablename__ = "medication_reminders"
    
    id              = Column(Integer, primary_key=True, index=True)
    patient_id      = Column(Integer, nullable=False, index=True)
    patient_source  = Column(String(50), nullable=False) # 'registered' or 'master'
    rx_id           = Column(Integer, nullable=True)
    medicine_name   = Column(String(255), nullable=False)
    reminder_time   = Column(Time, nullable=True)
    total_stock     = Column(Integer, default=0)
    remaining_stock = Column(Integer, default=0)
    is_active       = Column(Boolean, default=True)
    
    # We do not define FK to medication_logs here because the relationship is loaded locally if needed,
    # or just keep it simple. Let's add the logs relationship if we need it.

class MedicationLog(Base):
    __tablename__ = "medication_logs"
    
    id          = Column(Integer, primary_key=True, index=True)
    reminder_id = Column(Integer, nullable=False, index=True)
    patient_id  = Column(Integer, nullable=False, index=True)
    status      = Column(String(20), nullable=False) # 'taken', 'missed'
    taken_at    = Column(DateTime, nullable=True)
    log_date    = Column(Date, nullable=False)
    
