/*==============================================================*/
/* Nom de SGBD :  MySQL 5.0                                     */
/* Date de création :  23/03/2020 15:26:30                      */
/*==============================================================*/


drop table if exists ADHERENTS;

drop table if exists BD;

drop table if exists BIBLIOTHEQUE;

drop table if exists DICTIONNAIRES;

drop table if exists DOCUMENTS;

drop table if exists JOURNAUX;

drop table if exists LIVRES;

drop table if exists VOLUMES;

/*==============================================================*/
/* Table : ADHERENTS                                            */
/*==============================================================*/
create table ADHERENTS
(
   ID_ADHE              int not null,
   ID_BIBLIO            int not null,
   NOM                  char(20),
   PRENOM               char(20),
   INSCRIT              bool,
   DATE                 date,
   primary key (ID_ADHE)
);

/*==============================================================*/
/* Table : BD                                                   */
/*==============================================================*/
create table BD
(
   ID_BD                int not null,
   ID_VOLUME            int not null,
   DESTINATAIRE         char(30),
   primary key (ID_BD)
);

/*==============================================================*/
/* Table : BIBLIOTHEQUE                                         */
/*==============================================================*/
create table BIBLIOTHEQUE
(
   ID_BIBLIO            int not null,
   primary key (ID_BIBLIO)
);

/*==============================================================*/
/* Table : DICTIONNAIRES                                        */
/*==============================================================*/
create table DICTIONNAIRES
(
   ID_DICO              int not null,
   ID_VOLUME            int not null,
   primary key (ID_DICO)
);

/*==============================================================*/
/* Table : DOCUMENTS                                            */
/*==============================================================*/
create table DOCUMENTS
(
   ID_DOC               int not null,
   ID_BIBLIO            int not null,
   TITRE                char(50),
   primary key (ID_DOC)
);

/*==============================================================*/
/* Table : JOURNAUX                                             */
/*==============================================================*/
create table JOURNAUX
(
   ID_JOURN             int not null,
   ID_DOC               int not null,
   DATE_DE_PARUTION     date,
   primary key (ID_JOURN)
);

/*==============================================================*/
/* Table : LIVRES                                               */
/*==============================================================*/
create table LIVRES
(
   ID_LIVRE             int not null,
   ID_ADHE              int null,
   ID_VOLUME            int not null,
   primary key (ID_LIVRE)
);

/*==============================================================*/
/* Table : VOLUMES                                              */
/*==============================================================*/
create table VOLUMES
(
   ID_VOLUME            int not null,
   ID_DOC               int not null,
   AUTEUR               char(30),
   primary key (ID_VOLUME)
);

alter table ADHERENTS add constraint FK_INSCRIT foreign key (ID_BIBLIO)
      references BIBLIOTHEQUE (ID_BIBLIO) on delete restrict on update restrict;

alter table BD add constraint FK_A_POUR_BD foreign key (ID_VOLUME)
      references VOLUMES (ID_VOLUME) on delete restrict on update restrict;

alter table DICTIONNAIRES add constraint FK_A_POUR_DICO foreign key (ID_VOLUME)
      references VOLUMES (ID_VOLUME) on delete restrict on update restrict;

alter table DOCUMENTS add constraint FK_AJOUTE foreign key (ID_BIBLIO)
      references BIBLIOTHEQUE (ID_BIBLIO) on delete restrict on update restrict;

alter table JOURNAUX add constraint FK_A_POUR_JOURNAUX foreign key (ID_DOC)
      references DOCUMENTS (ID_DOC) on delete restrict on update restrict;

alter table LIVRES add constraint FK_ASSOCIATION_9 foreign key (ID_ADHE)
      references ADHERENTS (ID_ADHE) on delete restrict on update restrict;

alter table LIVRES add constraint FK_A_POUR_LIVRE foreign key (ID_VOLUME)
      references VOLUMES (ID_VOLUME) on delete restrict on update restrict;

alter table VOLUMES add constraint FK_A_POUR_VOLUME foreign key (ID_DOC)
      references DOCUMENTS (ID_DOC) on delete restrict on update restrict;

