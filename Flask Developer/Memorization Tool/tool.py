# write your code here
from sqlalchemy import create_engine, Integer, String, Column
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///flashcard.db?check_same_thread=False')


class FlashCards(Base):
    __tablename__ = 'flashcard'

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    box_number = Column(Integer)


Base.metadata.create_all(engine)
Session = sessionmaker(engine)
session = Session()


def add_flashcards():
    while (inp := input('\n1. Add a new flashcard\n2. Exit\n')) != '2':
        if inp == '1':
            while (question := input('\nQuestion:\n')).strip() == '':
                ...
            while (answer := input('Answer:\n')).strip() == '':
                ...
            session.add(FlashCards(question=question, answer=answer, box_number=1))
            session.commit()
        else:
            print(f'{inp} is not an option\n')
    print()


def practice_flashcards():
    cards = session.query(FlashCards).all()
    if len(cards) == 0:
        print('There is no flashcard to practice!\n')
    else:
        for i in cards:
            print(f'Question: {i.question}')
            while (inp := input('press "y" to see the answer:\npress "n" to skip:\npress "u" to update:\n')) not in 'yun':
                print(f'{inp} is not an option')
            if inp == 'y':
                print(f'\nAnswer: {i.answer}')
                while (your_answer := input('press "y" if your answer is correct:\npress "n" if your answer is wrong:\n')) not in 'ny':
                    print(f'{your_answer} is not an option')
                if your_answer == 'y':
                    if i.box_number == 3:
                        session.query(FlashCards).filter(FlashCards.id == i.id).delete()
                    else:
                        session.query(FlashCards).filter(FlashCards.id == i.id).update(
                            {FlashCards.box_number: i.box_number+1})
                    session.commit()
                else:
                    session.query(FlashCards).filter(FlashCards.id == i.id).update(
                        {FlashCards.box_number: 1})
                    session.commit()
            elif inp == 'u':
                update(i.id, i.question, i.answer)


def update(id_question, question, answer):
    while (inp := input('press "d" to delete the flashcard:\npress "e" to edit the flashcard:\n')) not in 'ed':
        print(f'{inp} is not an option')
    if inp == 'e':
        print(f"current question: {question}")
        new_question = input('please write a new question:\n')
        session.query(FlashCards).filter(FlashCards.id == id_question).update({FlashCards.question: new_question})
        print(f'current answer: {answer}')
        new_answer = input('please write a new answer:\n')
        session.query(FlashCards).filter(FlashCards.id == id_question).update({FlashCards.answer: new_answer})
        session.commit()
    else:
        session.query(FlashCards).filter(FlashCards.id == id_question).delete()
        session.commit()


if __name__ == '__main__':
    d = {'1': add_flashcards, '2': practice_flashcards}
    while (inp := input("1. Add flashcards\n2. Practice flashcards\n3. Exit\n")) != '3':
        if inp in d:
            d[inp]()
        else:
            print(f'{inp} is not an option\n')
    else:
        print('Bye!')
