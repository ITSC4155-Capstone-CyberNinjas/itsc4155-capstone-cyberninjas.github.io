# schemas.py
from datetime import datetime 
from pydantic import BaseModel



class WifiCounts(BaseModel):
    timestamp: datetime
	Atki: int
	Auxi: int
	BaTF: int
	Band: int
	Barn: int
	BelG: int
	BelH: int
	Bioi: int
	Burs: int
	Cafe: int
	Came: int
	Cato: int
	Ceda: int
	CoEd: int
	Colv: int
	Cone: int
	Coun: int
	Denn: int
	Duke: int
	EPIC: int
	FOPS: int
	Faci: int
	Foun: int
	Fret: int
	Frid: int
	Gage: int
	Gari: int
	Grig: int
	Harr: int
	Heal: int
	Hick: int
	Hous: int
	HunH: int
	Irwi: int
	JBui: int
	Kenn: int
	King: int
	Laur: int
	Levi: int
	Lync: int
	MSII: int
	Macy: int
	Mart: int
	McCo: int
	McMi: int
	Memo: int
	MilH: int
	Milt: int
	NERF: int
	PORT: int
	Phil: int
	Pros: int
	Rece: int
	Rees: int
	Robi: int
	Rowe: int
	SVDH: int
	Scot: int
	Smit: int
	SoTF: int
	Stor: int
	StuA: int
	StuH: int
	StuU: int
	Syca: int
	Tenn: int
	UREC: int
	Unio: int
	Wach: int
	Wall: int
	Winn: int
	With: int
	Wood: int

	class Config:
        orm_mode = True