import gql from "graphql-tag";

const QUERY_ALL_JOBS = gql`
  query {
    allJobs {
      edges {
        node {
          id
          name
          deadline
          client {
            id
            firstName
            lastName
            businessName
          }
        }
      }
    }
  }
`;

const QUERY_ALL_CLIENTS = gql`
  query {
    allClients {
      edges {
        node {
          firstName
          lastName
          businessName
          id
          jobSet {
            edges {
              node {
                id
                name
                deadline
              }
            }
          }
          noteSet {
            edges {
              node {
                id
                title
                content
              }
            }
          }
        }
      }
    }
  }
`;

const QUERY_ALL_NOTES = gql`
  query {
    allNotes {
      edges {
        node {
          id
          title
          content
          client {
            id
            businessName
            firstName
            lastName
          }
          job {
            id
            name
          }
        }
      }
    }
  }
`;

const QUERY_ALL_TAGS = gql`
  query {
    allTags {
      edges {
        node {
          id
          name
          description
        }
      }
    }
  }
`;

const QUERY_ALL_PARTS = gql`
  query {
    allParts {
      edges {
        node {
          id
          name
          description
        }
      }
    }
  }
`;

const ALL_CLIENTS_AND_JOBS = gql`
  query {
    allJobs {
      edges {
        node {
          name
          id
        }
      }
    }
    allClients {
      edges {
        node {
          firstName
          lastName
          businessName
          id
        }
      }
    }
  }
`;

const ALL_NOTES_PARTS_JOBS = gql`
  query {
    allJobs {
      edges {
        node {
          name
          id
        }
      }
    }
    allNotes {
      edges {
        node {
          title
          id
        }
      }
    }
    allParts {
      edges {
        node {
          name
          id
        }
      }
    }
  }
`;

const DETAILED_JOB_BY_ID = gql`
  query job($id: ID!) {
    job(id: $id) {
      client {
        firstName
        lastName
        businessName
        id
      }
      id
      name
      complete
      labor
      description
      createdAt
      modifiedAt
      deadline
      noteSet {
        edges {
          node {
            title
            id
          }
        }
      }
      partSet {
        edges {
          node {
            name
            id
          }
        }
      }
    }
  }
`;

const DETAILED_CLIENT_BY_ID = gql`
  query client($id: ID!) {
    client(id: $id) {
      id
      businessName
      firstName
      lastName
      streetAddress
      city
      state
      zipcode
      email
      jobSet {
        edges {
          node {
            id
            name
            description
            deadline
          }
        }
      }
      noteSet {
        edges {
          node {
            id
            title
            content
            client {
              id
              businessName
              firstName
              lastName
            }
          }
        }
      }
    }
  }
`;

const DETAILED_NOTE_BY_ID = gql`
  query note($id: ID!) {
    note(id: $id) {
      id
      title
      content
      createdAt
      modifiedAt
      job {
        id
        name
        deadline
        client {
          businessName
          firstName
          lastName
          id
        }
      }
      client {
        id
        businessName
        firstName
        lastName
      }
    }
  }
`;

const DETAILED_TAG_BY_ID = gql`
  query tag($id: ID!) {
    tag(id: $id) {
      id
      name
      description
      createdAt
      modifiedAt
      job {
        name
        description
        id
      }
      part {
        name
        description
        id
      }
      note {
        title
        content
        id
      }
    }
  }
`;

const DETAILED_PART_BY_ID = gql`
  query($id: ID!) {
    part(id: $id) {
      id
      name
      description
      cost
      job {
        name
        id
      }
    }
  }
`;

const SETTINGS_QUERY = gql`
  query settings($id: ID!) {
    user(id: $id) {
      id
      firstName
      lastName
      streetAddress
      city
      state
      zipcode
      businessName
      premium
      paidUntil
      username
    }
    allClients {
      edges {
        node {
          id
        }
      }
    }
    allJobs {
      edges {
        node {
          id
        }
      }
    }
    allNotes {
      edges {
        node {
          id
        }
      }
    }
    allParts {
      edges {
        node {
          id
        }
      }
    }
    allTags {
      edges {
        node {
          id
        }
      }
    }
  }
`;

export {
  QUERY_ALL_JOBS,
  QUERY_ALL_NOTES,
  QUERY_ALL_TAGS,
  DETAILED_JOB_BY_ID,
  QUERY_ALL_CLIENTS,
  DETAILED_CLIENT_BY_ID,
  QUERY_ALL_PARTS,
  ALL_CLIENTS_AND_JOBS,
  DETAILED_NOTE_BY_ID,
  ALL_NOTES_PARTS_JOBS,
  DETAILED_TAG_BY_ID,
  DETAILED_PART_BY_ID,
  SETTINGS_QUERY
};
