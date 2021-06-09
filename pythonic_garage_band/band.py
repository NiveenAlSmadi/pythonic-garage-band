
class Band():

    all_band=[]

    def __init__(self,name,member):
        self.name=name 
        self.members=member
        Band.all_band.append(self)
    

    def play_solos(self):
        solo_list=[]
        for x in self.members:
            return solo_list


    def __str__(self):

        return f"{self.name}"

    def __repr__(self):

        return f"{self.name}"
        

    @classmethod
    def to_list(cls) :
      
        return cls.all_band




class Musician():

    def __str__(self):

        pass

    def __repr__(self):

        pass 

    def play_solo(self):

        pass 
    
    
class Guitarist(Musician):

    def __str__(self):

        pass

    def __repr__(self):

        pass 

    def get_instrument(self):

        return 'guitar'
    def play_solo(self):

        pass 


class Bassist(Musician): 

    def __str__(self):

        pass

    def __repr__(self):

        pass 

    def get_instrument(self):

        return 'bass'
    def play_solo(self):

        pass 


class  Drummer(Musician):

   def __str__(self):

        pass

   def __repr__(self):

        pass 

   def get_instrument(self):

        return 'drums'


   def play_solo(self):

        pass 
