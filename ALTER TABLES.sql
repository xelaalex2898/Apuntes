ALTER TABLE user_personal_info 
ADD IdRol INT,
    IdClient INT,
    FOREIGN KEY (IdClient) REFERENCES Clients(ClientId),
    FOREIGN KEY (IdRol) REFERENCES Rol(RolId);
-- TABLE USER PROFILE PHOTO
ALTER TABLE User_profile_photo 
ADD FOREIGN KEY (UserId) REFERENCES User_personal_info(UserpersonalinfoId);
-- TABLE USER notifications 
 