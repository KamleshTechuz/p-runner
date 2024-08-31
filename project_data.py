baseFolder = '/Documents'

actions = ['Open in VS Code', 'Run', "Open Folder"]

projects = [{
    "id": 1, "name": "Insyd", "children": [
        { "id": 1, "name": "Front", "path": f".{baseFolder}/insyd/insyd-react", "command": "nvm use && npm run dev"},
        { "id": 2, "name": "Node", "path": f".{baseFolder}/insyd/insyd-node", "command": "nvm use && yarn watch"},
    ]
}, {
    "id": 2, "name": "Oxford", "children": [
        { "id": 1, "name": "Admin", "path": f".{baseFolder}/oxford/admin", "command": "nvm use && yarn start"},
        { "id": 2, "name": "Front", "path": f".{baseFolder}/oxford/oxford-mtrain-react", "command": "nvm use && npm run dev"},
        { "id": 3, "name": "Node", "path": f".{baseFolder}/oxford/oxford-mtrain-node", "command": "nvm use && yarn watch"},
    ]
}, {
    "id": 3, "name": "Getlitt", "children": [
        { "id": 1, "name": "Admin", "path": f".{baseFolder}/getLitt/from-git/getlitt-angular-admin", "command": "nvm use && npm run start"},
        { "id": 2, "name": "Front", "path": f".{baseFolder}/getLitt/from-git/getlitt-angular-front", "command": "nvm use && npm run start"},
        { "id": 3, "name": "Node", "path": f".{baseFolder}/getLitt/from-git/getlitt-node", "command": "nvm use && node server.js"},
    ]
}, {
    "id": 3, "name": "DivorceX", "children": [
        { "id": 1, "name": "Admin", "path": f".{baseFolder}/divorceX/DivorceX-Admin-React", "command": "nvm use && yarn start"},
        { "id": 2, "name": "Front", "path": f".{baseFolder}/divorceX/DivorceX-React-ts", "command": "nvm use && npm run dev"},
        { "id": 3, "name": "Node", "path": f".{baseFolder}/divorceX/DivorceX-API", "command": "nvm use && yarn watch"},
    ]
}]

# Sort projects by name
projects.sort(key=lambda x: x['name'])