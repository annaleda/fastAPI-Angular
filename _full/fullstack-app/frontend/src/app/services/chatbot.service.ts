// chatbot.service.ts

import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ChatbotService {

  private apiUrl = 'http://localhost:8080/chat';  // URL del tuo backend FastAPI

  constructor(private http: HttpClient) {}

  // Funzione per inviare un messaggio al chatbot e ricevere la risposta
  sendMessage(message: string): Observable<any> {
    return this.http.post<any>(this.apiUrl, { message });
  }
}
