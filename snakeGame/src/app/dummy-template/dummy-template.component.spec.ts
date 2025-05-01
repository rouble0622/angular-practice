import { ComponentFixture, TestBed } from '@angular/core/testing';
import { DummyTemplateComponent } from './dummy-template.component';

describe('DummyTemplateComponent', () => {
  let component: DummyTemplateComponent;
  let fixture: ComponentFixture<DummyTemplateComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [DummyTemplateComponent]
    }).compileComponents();

    fixture = TestBed.createComponent(DummyTemplateComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });

  it('should have a title', () => {
    expect(component.title).toBe('Dummy Template');
  });

  it('should have items array', () => {
    expect(component.items.length).toBe(4);
  });
}); 