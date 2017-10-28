import { ProjectDefinition } from './types/common'

export const mockDefinition: ProjectDefinition = {
  modules: [
    {
      name: '',
      content: `\
# Welcome to Graphcool!
#
# This file is the main config file for your Graphcool Project.
# It's very minimal at this point and uses default values.
# We've included a hello world function here.
# Just uncomment it and run \`graphcool deploy\`
#
# Check out some examples:
#    github.com/graphcool/examples
#
# Happy Coding!


# GraphQL types
types: ./types.graphql


# uncomment this:

# functions:
#   hello:
#     handler:
#       code:
#         src: ./code/hello.js
#     type: resolver
#     schema: ./code/hello.graphql

 
# Graphcool modules
modules: {}


# Model/Relation permissions
permissions:
- operation: "*"

  
# Permanent Auth Token / Root Tokens
rootTokens: []

`,
      files: {
        './types.graphql': `\
# This file contains the GraphQL Types

# All types need to have the three fields id, updatedAt and createdAt like this:

type User implements Node {
  id: ID! @isUnique
  createdAt: DateTime!
  updatedAt: DateTime!
}


# Graphcool has one special type, the File type:

# type File implements Node {
#   contentType: String!
#   createdAt: DateTime!
#   id: ID! @isUnique
#   name: String!
#   secret: String! @isUnique
#   size: Int!
#   updatedAt: DateTime!
#   url: String! @isUnique
# }
`,
        './code/hello.js': `\
module.exports = event => {
  return {
    data: {
      message: \`Hello $\{event.data.name || 'World'\}\`
    }
  }
}`,
        './code/hello.graphql': `\
type HelloPayload {
  message: String!
}

extend type Query {
  hello(name: String): HelloPayload
}
`,
      },
    },
  ],
}

export const mockEnv = {
  default: 'dev',
  environments: {
    dev: 'cj84dopd3197p01200l5sb9fs',
  },
}
