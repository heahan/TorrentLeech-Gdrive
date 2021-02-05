from tobrot.sample_config import Config

#Fill your all data, read readme for reference

#FOR CUSTOM COMMANDS READ REAME AND FILL THEM...

class Config(Config):
        TG_BOT_TOKEN= "1671340816:AAG2RUyHa795nWXQDeNhjXGpnzf678Zs7IE"
            APP_ID = 2349847
                API_HASH = "ba712182c38536fc7ce235f972834eb3"
                    OWNER_ID = 1473490396
                        AUTH_CHANNEL = [-1001463269462]
                            DESTINATION_FOLDER = "TorrentLeech-Gdrive" #Name of your folder read readme(not id of the folder)
                                #Just don't fill RCLONE_CONFIG vars, insted copy your rclone.conf file in root directory
                                    #if your wanted to fill -- fill your rclone config like this(Your config may have some extra value or less. so Don't worry)
                                        RCLONE_CONFIG = """
                                        [DRIVE]
                                        type = drive
                                        client_id = 28dslkgjsdl-fill-your-details-apps.googleusercontent.com
                                        client_secret = 6Tib48-fill-your-details-KuXXDX-eWgnRBYc
                                        scope = drive
                                        root_folder_id =
                                        token = {"access_token":"ya29.a-fill-your-details-af4ychuHswBt8X0nf2oWmczsHg6MYPSE6hXo-PJ-fill-your-details-s06KAecfw_H-tYThBtbs:20:25.430920315Z"}
                                        team_drive = 0AB0q-fill-your-details-sdrgsgsdUk9PVA
                                        """
                                        
