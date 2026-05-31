[Setup]
AppName=ExpectShop
AppVersion=1.0
AppPublisher=IvanElCrack
DefaultDirName={autopf}\ExpectShop
DefaultGroupName=ExpectShop
OutputDir=Instalador
OutputBaseFilename=ExpectShopInstaller
SetupIconFile=Assets\logotipo.ico
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Tasks]
Name: "desktopicon"; Description: "Crear acceso directo en el escritorio"; GroupDescription: "Iconos adicionales"

[Files]
Source: "dist\ExpectShop\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs

[Icons]
Name: "{group}\ExpectShop"; Filename: "{app}\ExpectShop.exe"
Name: "{group}\Desinstalar ExpectShop"; Filename: "{uninstallexe}"
Name: "{commondesktop}\ExpectShop"; Filename: "{app}\ExpectShop.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\ExpectShop.exe"; Description: "Iniciar ExpectShop"; Flags: nowait postinstall skipifsilent