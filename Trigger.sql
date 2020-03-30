CREATE DEFINER=root@localhost TRIGGER bibliotheque.livres_BEFORE_UPDATE BEFORE UPDATE ON livres FOR EACH ROW

BEGIN
    IF (select count(ID_LIVRE) from livres where ID_ADHE = new.ID_ADHE) >= 3 
    then
      set @msg = '3 livres maximum: ';
    signal sqlstate '45000' set message_text = @msg;
    end if;
END