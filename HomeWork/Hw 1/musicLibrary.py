#Corey Henry                                 #Date Assigned: 
#                                            #
#Course CSE 1384 Sec 06                      #Date Due: 
#File name: Lab 
#
#Program description-

class MusicLibrary():
    def __init__(self):

        self.library = []
   
    def add_item(self, CD):
        self.library.append(CD)
        

    def remove_item(self,CD):
        count = 0
        for each_line in CD:
            each_line = each_line.strip()
            count += 1
            if count == 1:
                self.artist_list.remove(each_line)
            elif count == 2:
                self.album_list.remove(each_line)
            elif count == 3:
                self.genre_list.remove(each_line)
            elif count >= 4:
                self.song_list.remove(each_line)
        

    def get_list(self,CD):
        count = 0
        name = CD.linestrip
        for each in artist_list:
            if each == name:
                arist = name
            else:
                count +=1
        #create the print and use the len to figure out what CD it is, len is the count
        album = self.album_list[count]
        songs=[]
        for each in self.song_list[count]:
            self.songs.append(each)
        
            
        
        
        
        

   

    def generate_genre_list(self, genre):
        count = 0
        album_numbers = []
        albums = []
        for each_line in self.genre_list:
            if each_line == genre:
                albumb_numbers.append(count)
                count +=1
            else:
                count +=1
        for each in album_numbers:
            albums.append(self.album_list[each])
        return(albumbs)
            
                
        
