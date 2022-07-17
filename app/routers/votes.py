from .. import models, schemas, utils, oauth2
from fastapi import  Response, status, HTTPException, Depends, APIRouter
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List

from app import database

router = APIRouter(
    prefix = "/vote",
    tags = ["votes"]
)

@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote : schemas.Vote, db : Session = Depends(database.get_db), current_user: int = Depends(oauth2.get_current_user)):
    
    post = db.query(models.Post).filter(models.Post.id == vote.post_id)
    if not post :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, details = f"there is no post with the id of {vote.post_id}")
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    found_vote = vote_query.first()
    if (vote.dir == 1) :
        if found_vote :
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail = f"user {current_user.id} has already voted on a post with the id of {vote.post_id}")
        new_vote = models.Vote(post_id = vote.post_id, user_id = current_user.id)
        db.add(new_vote)
        db.commit()
        return{"message":"vote successfully added"}

    else : 
        if not found_vote :
            raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail = f"user {current_user.id} dosen't have a vote on a post with the id of {vote.post_id}")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return{"message":"vote successfuly deleted"}
        