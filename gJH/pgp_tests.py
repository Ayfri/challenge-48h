import pgpy

message = pgpy.PGPMessage.from_blob("""
-----BEGIN PGP MESSAGE-----

wcFMAyiZ01Nne++QAQ//XdcPKURt+QsJdcwPpRNnlWd5oOTKJNQWi8cf5YA1wDGL
K7fKPkvfRUqqzaerV3XrEW35QXk7D7FE9ATl4be7fxroiX/s/ybGV2Y6BhSYBd1G
jXLQcrHZGBQNDFx4SgMmvLEMxBWlkAPdYTNp+O8mjesRXNB8HTQoFNcDClCCruuu
Rc7Qagshn3RR3DGcBvVlWauNU+kUQYtyPaUd/xECh5oDs9ELn4MdO6Pyu77rboZ/
HQVQegUAGR89rtnY588/Eh4fwfccvFGcLRAOotzt5OZ53tYRJ8+HOWnT1KnJ1Y45
ICyk/XmDQnJwuITWG08y+ef0c9zm62gf+Z3AcanKAU/7H66stIZxIGkG2DLHNWRr
2vuZqhsJ49zqrDAP1CsH5GGSItbwyd8H4CoD2b150rERzK9qUr5ZyJEslWwYnlR7
ug+0l0XAipyPJvQqWDEV8ZMY21fgpb6CCmYsh6+6dz3pVMx0xO9UUPLCci2mMTKT
re4Tqm78tSBa3ipeBnMJzrtziUcI3pWUHCJwqXsRyMs2RgQhrJeOgibQGT/DnfLn
TwNRoky33w4qdWCe4V2tiTK1JvXFmVqQ5ov7kZEE+wphD8MuC05ffjJn5DowFC2/
sbReFJ9AolVYfUz1PREMF1qjUWfba85umO9DQr7ndbUKFfJZ6tqjAPhK5hwXkp7S
NwHC1ZggJvHUSuzkVWUyDGgTsZdSqNUGdGevsJjw1JTcQ+yjP/wuQuxRzjQLuCEh
hDUdePEZliw=
=Ax3p
-----END PGP MESSAGE-----""")

private_key, _ = pgpy.PGPKey.from_file("secret.asc")
print(private_key.decrypt(message).message)
