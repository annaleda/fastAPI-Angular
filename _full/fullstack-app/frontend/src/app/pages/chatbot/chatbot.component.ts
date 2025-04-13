import { Component, OnInit } from '@angular/core';
import { ChatbotService } from '../../services/chatbot.service';

@Component({
  selector: 'app-chatbot',
  templateUrl: './chatbot.component.html',
  styleUrls: ['./chatbot.component.css']
})
export class ChatbotComponent implements OnInit {

   message: string = '';
  response: string = '';

  constructor(private chatbotService: ChatbotService) {}

  sendMessage() {
    if (this.message.trim()) {
      this.chatbotService.sendMessage(this.message).subscribe((data) => {
        this.response = data.response;
      });
    }
  }

}
