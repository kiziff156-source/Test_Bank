from sqlalchemy.orm import Session
from src.main.api.db.models.credit_table import Credit


class CreditCrudDb:
    @staticmethod
    def get_credit_from_db_by_credit_id(db: Session, credit_id: int) -> Credit:
        return db.query(Credit).filter_by(id = credit_id).first()

    @staticmethod
    def get_credit_from_db_by_account_id(db:Session, account_id: int) -> Credit:
        return db.query(Credit).filter_by(account_id = account_id).first()

    @staticmethod
    def get_credits_from_db_by_account_id(db:Session, account_id: int) -> list[Account]:
        return db.query(Credit).filter_by(account_id = account_id).order_by(Credit.account_id).limit(2).all()
