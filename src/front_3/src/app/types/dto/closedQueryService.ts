export interface ClosedQueryRequest {
  query: string;
}

export interface ClosedQueryResponse {
  //context: string[];
  answer: string;
  audioFileName : string;
  pdfFileNames : string[];
}
